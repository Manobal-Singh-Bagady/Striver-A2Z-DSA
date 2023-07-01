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
    def transpose(self, arr, n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, a, n):
        for i in a:
            i.reverse()
        for i in range(n):
            for j in range(n):
                if i<j:
                    a[i][j], a[j][i] = a[j][i], a[i][j]

        # self.transpose(a,n)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = line1[k]
                k += 1
        obj = Solution()
        obj.rotateby90(matrix, n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
        print()

# } Driver Code Ends
