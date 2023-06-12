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


# m is maximum of number zeroes allowed
# to flip, n is size of array
def findZeroes(arr, n, m):
    l = 0
    r = 0
    best_win = 0
    count = 0
    while r < n:
        if count <= m:
            if arr[r] == 0:
                count += 1
            r += 1
        if count > m:
            if arr[l] == 0:
                count -= 1
            l += 1
        best_win = max(r - l, best_win)

    return best_win


# {
# Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        m = int(input())
        ans = findZeroes(arr, n, m)
        print(ans)
        tc = tc - 1
# } Driver Code Ends
