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


# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def findK(self, a, n, m, k):
        t = l = 0
        b = n - 1
        r = m - 1
        count = 0
        while t <= b and l <= r:
            for i in range(l, r + 1):
                count += 1
                if count == k:
                    return a[t][i]
            t += 1
            for i in range(t, b + 1):
                count += 1
                if count == k:
                    return a[i][r]
            r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    count += 1
                    if count == k:
                        return a[b][i]
            b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    count += 1
                    if count == k:
                        return a[i][l]
            l += 1


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])] for j in range(n[0])]
        c = 0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c += 1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends
