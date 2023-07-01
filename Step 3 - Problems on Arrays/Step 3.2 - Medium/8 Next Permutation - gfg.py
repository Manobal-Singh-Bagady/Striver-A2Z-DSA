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
    def nextPermutation(self, N, arr):
        index = -1
        for i in range(N - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                index = i
                break
        if index == -1:
            return arr[::-1]
        for i in range(N - 1, index, -1):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
                break
        return arr[: index + 1] + arr[:index:-1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
