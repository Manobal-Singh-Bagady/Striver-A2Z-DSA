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
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low >= high:
            return
        partition = self.partition(arr, low, high)
        self.quickSort(arr, low, partition - 1)
        self.quickSort(arr, partition + 1, high)

    def partition(self, arr, low, high):
        p = arr[high]
        i = low
        j = high - 1
        while i <= j:
            if arr[i] <= p:
                i += 1
            if arr[j] >= p:
                j -= 1
            if arr[i] > p and arr[j] < p and i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[high], arr[i] = arr[i], arr[high]
        return i


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
