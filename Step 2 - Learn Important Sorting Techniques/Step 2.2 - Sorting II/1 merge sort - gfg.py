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
    def merge(self, arr, l, m, r):
        ans = []
        i = l
        j = m + 1
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                ans.append(arr[i])
                i+=1
            else:
                ans.append(arr[j])
                j+=1
        while i <= m:
            ans.append(arr[i])
            i+=1
        while j <= r:
            ans.append(arr[j])
            j+=1
        arr[l : r + 1] = ans[:]

    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)


# {
# Driver Code Starts
# Initial Template for Python 3


import sys

input = sys.stdin.readline
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().mergeSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
