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
# User function template for Python


class Solution:
    def remove_duplicate(self, A, N):
        p = 0
        for i in range(1, N):
            if A[p] != A[i]:
                A[p + 1] = A[i]
                p += 1
        return p + 1


# {
# Driver Code Starts
# Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A, N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends
