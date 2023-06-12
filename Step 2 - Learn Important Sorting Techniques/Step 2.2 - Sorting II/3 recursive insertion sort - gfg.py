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

# Sort the array using insertion sort


class Solution:
    def insert(self, alist, index, n):
        if index == n - 1:
            return

        for i in range(index, -1, -1):
            if alist[i + 1] > alist[i]:
                break
            alist[i], alist[i + 1] = alist[i + 1], alist[i]

        self.insert(alist, index + 1, n)

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        self.insert(alist, 0, n)


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        Solution().insertionSort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()
# } Driver Code Ends
